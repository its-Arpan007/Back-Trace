import 'package:flutter_riverpod/flutter_riverpod.dart';

class LearningSessionState {
  final String sessionMode; // adaptive, revision, challenge, exam, quick, concept, mixed
  final int questionCount;

  const LearningSessionState({
    this.sessionMode = 'adaptive',
    this.questionCount = 5,
  });

  LearningSessionState copyWith({String? sessionMode, int? questionCount}) {
    return LearningSessionState(
      sessionMode: sessionMode ?? this.sessionMode,
      questionCount: questionCount ?? this.questionCount,
    );
  }
}

class LearningSessionNotifier extends StateNotifier<LearningSessionState> {
  LearningSessionNotifier() : super(const LearningSessionState());

  void setSessionMode(String mode) {
    state = state.copyWith(sessionMode: mode);
  }
}

final learningSessionProvider = StateNotifierProvider<LearningSessionNotifier, LearningSessionState>((ref) {
  return LearningSessionNotifier();
});
