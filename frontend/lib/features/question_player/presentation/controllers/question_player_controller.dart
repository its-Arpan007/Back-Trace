import 'package:flutter_riverpod/flutter_riverpod.dart';

class QuestionPlayerState {
  final int currentQuestionIndex;
  final int totalQuestions;
  final String selectedAnswer;
  final int confidenceScore; // 1-5
  final bool hintUnlocked;
  final bool isBookmarked;
  final int timeSpentSeconds;

  const QuestionPlayerState({
    this.currentQuestionIndex = 0,
    this.totalQuestions = 3,
    this.selectedAnswer = "0x1005",
    this.confidenceScore = 4,
    this.hintUnlocked = false,
    this.isBookmarked = false,
    this.timeSpentSeconds = 45,
  });

  QuestionPlayerState copyWith({
    int? currentQuestionIndex,
    int? totalQuestions,
    String? selectedAnswer,
    int? confidenceScore,
    bool? hintUnlocked,
    bool? isBookmarked,
    int? timeSpentSeconds,
  }) {
    return QuestionPlayerState(
      currentQuestionIndex: currentQuestionIndex ?? this.currentQuestionIndex,
      totalQuestions: totalQuestions ?? this.totalQuestions,
      selectedAnswer: selectedAnswer ?? this.selectedAnswer,
      confidenceScore: confidenceScore ?? this.confidenceScore,
      hintUnlocked: hintUnlocked ?? this.hintUnlocked,
      isBookmarked: isBookmarked ?? this.isBookmarked,
      timeSpentSeconds: timeSpentSeconds ?? this.timeSpentSeconds,
    );
  }
}

class QuestionPlayerNotifier extends StateNotifier<QuestionPlayerState> {
  QuestionPlayerNotifier() : super(const QuestionPlayerState());

  void selectAnswer(String val) => state = state.copyWith(selectedAnswer: val);
  void setConfidence(int val) => state = state.copyWith(confidenceScore: val);
  void unlockHint() => state = state.copyWith(hintUnlocked: true);
  void toggleBookmark() => state = state.copyWith(isBookmarked: !state.isBookmarked);
}

final questionPlayerProvider = StateNotifierProvider<QuestionPlayerNotifier, QuestionPlayerState>((ref) {
  return QuestionPlayerNotifier();
});
