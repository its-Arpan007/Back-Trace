import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/mastery_service.dart';

final frontendMasteryServiceProvider = Provider<FrontendMasteryService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendMasteryService(apiClient);
});

class MasteryState {
  final bool isLoading;
  final Map<String, dynamic>? summary;
  final Map<String, dynamic>? timeline;
  final List<dynamic>? predictions;
  final String? errorMessage;

  const MasteryState({
    required this.isLoading,
    this.summary,
    this.timeline,
    this.predictions,
    this.errorMessage,
  });

  MasteryState copyWith({
    bool? isLoading,
    Map<String, dynamic>? summary,
    Map<String, dynamic>? timeline,
    List<dynamic>? predictions,
    String? errorMessage,
  }) {
    return MasteryState(
      isLoading: isLoading ?? this.isLoading,
      summary: summary ?? this.summary,
      timeline: timeline ?? this.timeline,
      predictions: predictions ?? this.predictions,
      errorMessage: errorMessage,
    );
  }
}

class MasteryNotifier extends StateNotifier<MasteryState> {
  final FrontendMasteryService _service;

  MasteryNotifier(this._service) : super(const MasteryState(isLoading: false)) {
    loadMasterySummary("11111111-1111-1111-1111-111111111111");
  }

  Future<void> loadMasterySummary(String studentId) async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getStudentMasterySummary(studentId);
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(isLoading: false, summary: res['data'] as Map<String, dynamic>);
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }

  Future<void> loadTimeline(String studentId, {String conceptCode = 'DSA_ARRAYS_01'}) async {
    try {
      final res = await _service.getLearningTimeline(studentId, conceptCode: conceptCode);
      if (res['success'] == true) {
        state = state.copyWith(timeline: res['data'] as Map<String, dynamic>);
      }
    } catch (_) {}
  }
}

final masteryProvider = StateNotifierProvider<MasteryNotifier, MasteryState>((ref) {
  final service = ref.watch(frontendMasteryServiceProvider);
  return MasteryNotifier(service);
});
