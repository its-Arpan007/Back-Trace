import 'package:flutter_riverpod/flutter_riverpod.dart';

class AssessmentBuilderState {
  final String title;
  final List<String> selectedConcepts;
  final int questionCount;

  const AssessmentBuilderState({
    this.title = "Array Stride Quiz #1",
    this.selectedConcepts = const ["DSA_ARRAYS_01"],
    this.questionCount = 5,
  });

  AssessmentBuilderState copyWith({String? title, List<String>? selectedConcepts, int? questionCount}) {
    return AssessmentBuilderState(
      title: title ?? this.title,
      selectedConcepts: selectedConcepts ?? this.selectedConcepts,
      questionCount: questionCount ?? this.questionCount,
    );
  }
}

class AssessmentBuilderNotifier extends StateNotifier<AssessmentBuilderState> {
  AssessmentBuilderNotifier() : super(const AssessmentBuilderState());

  void setTitle(String text) => state = state.copyWith(title: text);
}

final assessmentBuilderProvider = StateNotifierProvider<AssessmentBuilderNotifier, AssessmentBuilderState>((ref) {
  return AssessmentBuilderNotifier();
});
