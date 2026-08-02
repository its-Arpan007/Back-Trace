import 'package:flutter_riverpod/flutter_riverpod.dart';

class ProgressState {
  final double overallMastery;
  final double learningVelocity;
  final int streakDays;

  const ProgressState({
    this.overallMastery = 0.785,
    this.learningVelocity = 1.45,
    this.streakDays = 7,
  });
}

final progressProvider = StateNotifierProvider<ProgressNotifier, ProgressState>((ref) {
  return ProgressNotifier();
});

class ProgressNotifier extends StateNotifier<ProgressState> {
  ProgressNotifier() : super(const ProgressState());
}
