import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/ai_service.dart';

final frontendAIServiceProvider = Provider<FrontendAIService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendAIService(apiClient);
});

class AIChatMessage {
  final String sender; // user or ai
  final String text;
  final bool grounded;

  AIChatMessage({required this.sender, required this.text, this.grounded = true});
}

class AIChatState {
  final bool isLoading;
  final List<AIChatMessage> messages;
  final String selectedProvider;

  const AIChatState({
    required this.isLoading,
    this.messages = const [],
    this.selectedProvider = 'gemini',
  });

  AIChatState copyWith({
    bool? isLoading,
    List<AIChatMessage>? messages,
    String? selectedProvider,
  }) {
    return AIChatState(
      isLoading: isLoading ?? this.isLoading,
      messages: messages ?? this.messages,
      selectedProvider: selectedProvider ?? this.selectedProvider,
    );
  }
}

class AIChatNotifier extends StateNotifier<AIChatState> {
  final FrontendAIService _service;

  AIChatNotifier(this._service) : super(const AIChatState(isLoading: false));

  Future<void> sendMessage(String text, String userId) async {
    final updated = List<AIChatMessage>.from(state.messages)..add(AIChatMessage(sender: 'user', text: text));
    state = state.copyWith(isLoading: true, messages: updated);

    try {
      final res = await _service.sendChatMessage(userId, text, provider: state.selectedProvider);
      final data = res['data'] as Map<String, dynamic>?;
      final replyText = data?['reply'] ?? "I understand your query based on your diagnostic results.";

      final finalMessages = List<AIChatMessage>.from(state.messages)..add(AIChatMessage(sender: 'ai', text: replyText));
      state = state.copyWith(isLoading: false, messages: finalMessages);
    } catch (e) {
      final finalMessages = List<AIChatMessage>.from(state.messages)..add(AIChatMessage(sender: 'ai', text: "Error: $e"));
      state = state.copyWith(isLoading: false, messages: finalMessages);
    }
  }
}

final aiChatProvider = StateNotifierProvider<AIChatNotifier, AIChatState>((ref) {
  final service = ref.watch(frontendAIServiceProvider);
  return AIChatNotifier(service);
});
