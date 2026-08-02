import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/question_service.dart';

final frontendQuestionServiceProvider = Provider<FrontendQuestionService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendQuestionService(apiClient);
});

class QuestionListState {
  final bool isLoading;
  final List<dynamic> questions;
  final String? errorMessage;

  const QuestionListState({required this.isLoading, this.questions = const [], this.errorMessage});

  QuestionListState copyWith({bool? isLoading, List<dynamic>? questions, String? errorMessage}) {
    return QuestionListState(
      isLoading: isLoading ?? this.isLoading,
      questions: questions ?? this.questions,
      errorMessage: errorMessage,
    );
  }
}

class QuestionListNotifier extends StateNotifier<QuestionListState> {
  final FrontendQuestionService _service;

  QuestionListNotifier(this._service) : super(const QuestionListState(isLoading: false)) {
    loadQuestions();
  }

  Future<void> loadQuestions() async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getQuestions();
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(isLoading: false, questions: res['data'] as List<dynamic>);
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final questionListProvider = StateNotifierProvider<QuestionListNotifier, QuestionListState>((ref) {
  final service = ref.watch(frontendQuestionServiceProvider);
  return QuestionListNotifier(service);
});
