import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/teacher_service.dart';

final frontendTeacherServiceProvider = Provider<FrontendTeacherService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendTeacherService(apiClient);
});

class TeacherDashboardState {
  final bool isLoading;
  final List<dynamic> classes;
  final List<dynamic> interventions;
  final String? errorMessage;

  const TeacherDashboardState({
    required this.isLoading,
    this.classes = const [],
    this.interventions = const [],
    this.errorMessage,
  });

  TeacherDashboardState copyWith({
    bool? isLoading,
    List<dynamic>? classes,
    List<dynamic>? interventions,
    String? errorMessage,
  }) {
    return TeacherDashboardState(
      isLoading: isLoading ?? this.isLoading,
      classes: classes ?? this.classes,
      interventions: interventions ?? this.interventions,
      errorMessage: errorMessage,
    );
  }
}

class TeacherDashboardNotifier extends StateNotifier<TeacherDashboardState> {
  final FrontendTeacherService _service;

  TeacherDashboardNotifier(this._service) : super(const TeacherDashboardState(isLoading: false)) {
    loadDashboard();
  }

  Future<void> loadDashboard() async {
    state = state.copyWith(isLoading: true);
    try {
      final classRes = await _service.getTeacherClasses();
      final intervRes = await _service.getInterventions();

      state = state.copyWith(
        isLoading: false,
        classes: (classRes['data'] as List?) ?? [],
        interventions: (intervRes['data'] as List?) ?? [],
      );
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final teacherDashboardProvider = StateNotifierProvider<TeacherDashboardNotifier, TeacherDashboardState>((ref) {
  final service = ref.watch(frontendTeacherServiceProvider);
  return TeacherDashboardNotifier(service);
});
