import 'package:flutter_riverpod/flutter_riverpod.dart';

class ReflectionState {
  final String whyChoice;
  final String confusionLog;
  final bool isSubmitted;

  const ReflectionState({
    this.whyChoice = "I added base address directly to index without multiplying by 4.",
    this.confusionLog = "Confused stride length with array length.",
    this.isSubmitted = false,
  });

  ReflectionState copyWith({String? whyChoice, String? confusionLog, bool? isSubmitted}) {
    return ReflectionState(
      whyChoice: whyChoice ?? this.whyChoice,
      confusionLog: confusionLog ?? this.confusionLog,
      isSubmitted: isSubmitted ?? this.isSubmitted,
    );
  }
}

class ReflectionNotifier extends StateNotifier<ReflectionState> {
  ReflectionNotifier() : super(const ReflectionState());

  void setWhyChoice(String text) => state = state.copyWith(whyChoice: text);
  void setConfusionLog(String text) => state = state.copyWith(confusionLog: text);
  void submitReflection() => state = state.copyWith(isSubmitted: true);
}

final reflectionProvider = StateNotifierProvider<ReflectionNotifier, ReflectionState>((ref) {
  return ReflectionNotifier();
});
