import 'package:flutter_riverpod/flutter_riverpod.dart';

class StudentDashboardState {
  final bool isLoading;
  final String studentName;
  final int streakDays;
  final double overallMasteryPct;
  final List<String> weakConcepts;
  final String motivationalInsight;

  const StudentDashboardState({
    required this.isLoading,
    this.studentName = "Alex",
    this.streakDays = 7,
    this.overallMasteryPct = 78.5,
    this.weakConcepts = const ["DSA_ARRAYS_01", "DSA_TREES_01"],
    this.motivationalInsight = "Student mastery has increased by 18% over the last 14 days.",
  });

  StudentDashboardState copyWith({
    bool? isLoading,
    String? studentName,
    int? streakDays,
    double? overallMasteryPct,
    List<String>? weakConcepts,
    String? motivationalInsight,
  }) {
    return StudentDashboardState(
      isLoading: isLoading ?? this.isLoading,
      studentName: studentName ?? this.studentName,
      streakDays: streakDays ?? this.streakDays,
      overallMasteryPct: overallMasteryPct ?? this.overallMasteryPct,
      weakConcepts: weakConcepts ?? this.weakConcepts,
      motivationalInsight: motivationalInsight ?? this.motivationalInsight,
    );
  }
}

class StudentDashboardNotifier extends StateNotifier<StudentDashboardState> {
  StudentDashboardNotifier() : super(const StudentDashboardState(isLoading: false));

  void refreshDashboard() {
    state = state.copyWith(isLoading: true);
    Future.delayed(const Duration(milliseconds: 300), () {
      state = state.copyWith(isLoading: false);
    });
  }
}

final studentDashboardProvider = StateNotifierProvider<StudentDashboardNotifier, StudentDashboardState>((ref) {
  return StudentDashboardNotifier();
});
