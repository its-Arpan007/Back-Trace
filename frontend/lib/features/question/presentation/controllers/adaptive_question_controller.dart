import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/features/question/presentation/controllers/question_controller.dart';
import 'package:backtrace/services/question_service.dart';

class AdaptivePracticeState {
  final bool isLoading;
  final Map<String, dynamic>? practiceSet;
  final String? errorMessage;

  const AdaptivePracticeState({required this.isLoading, this.practiceSet, this.errorMessage});

  AdaptivePracticeState copyWith({bool? isLoading, Map<String, dynamic>? practiceSet, String? errorMessage}) {
    return AdaptivePracticeState(
      isLoading: isLoading ?? this.isLoading,
      practiceSet: practiceSet ?? this.practiceSet,
      errorMessage: errorMessage,
    );
  }
}

class AdaptivePracticeNotifier extends StateNotifier<AdaptivePracticeState> {
  final FrontendQuestionService _service;

  AdaptivePracticeNotifier(this._service) : super(const AdaptivePracticeState(isLoading: false));

  Future<void> generateSet(List<String> conceptCodes, String difficulty, int count) async {
    state = state.copyWith(isLoading: true);
    try {
      final reqData = {
        'concept_codes': conceptCodes,
        'difficulty': difficulty,
        'question_count': count,
        'adaptive': true,
      };
      final res = await _service.generatePracticeSet(reqData);
      if (res['success'] == true) {
        state = state.copyWith(isLoading: false, practiceSet: res['data'] as Map<String, dynamic>);
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final adaptivePracticeProvider = StateNotifierProvider<AdaptivePracticeNotifier, AdaptivePracticeState>((ref) {
  final service = ref.watch(frontendQuestionServiceProvider);
  return AdaptivePracticeNotifier(service);
});
