import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/curriculum_service.dart';

final frontendCurriculumServiceProvider = Provider<FrontendCurriculumService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendCurriculumService(apiClient);
});

class SubjectState {
  final bool isLoading;
  final List<dynamic> subjects;
  final String? errorMessage;

  const SubjectState({required this.isLoading, this.subjects = const [], this.errorMessage});

  SubjectState copyWith({bool? isLoading, List<dynamic>? subjects, String? errorMessage}) {
    return SubjectState(
      isLoading: isLoading ?? this.isLoading,
      subjects: subjects ?? this.subjects,
      errorMessage: errorMessage,
    );
  }
}

class SubjectNotifier extends StateNotifier<SubjectState> {
  final FrontendCurriculumService _service;

  SubjectNotifier(this._service) : super(const SubjectState(isLoading: false)) {
    loadSubjects();
  }

  Future<void> loadSubjects() async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getSubjects();
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(isLoading: false, subjects: res['data'] as List<dynamic>);
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message'] ?? 'Failed to load subjects');
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final subjectProvider = StateNotifierProvider<SubjectNotifier, SubjectState>((ref) {
  final service = ref.watch(frontendCurriculumServiceProvider);
  return SubjectNotifier(service);
});
