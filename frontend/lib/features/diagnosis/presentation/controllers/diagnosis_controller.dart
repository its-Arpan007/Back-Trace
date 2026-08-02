import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/diagnosis_service.dart';

final frontendDiagnosisServiceProvider = Provider<FrontendDiagnosisService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendDiagnosisService(apiClient);
});

class DiagnosisState {
  final bool isAnalyzing;
  final Map<String, dynamic>? activeReport;
  final Map<String, dynamic>? explanation;
  final String? errorMessage;

  const DiagnosisState({
    required this.isAnalyzing,
    this.activeReport,
    this.explanation,
    this.errorMessage,
  });

  DiagnosisState copyWith({
    bool? isAnalyzing,
    Map<String, dynamic>? activeReport,
    Map<String, dynamic>? explanation,
    String? errorMessage,
  }) {
    return DiagnosisState(
      isAnalyzing: isAnalyzing ?? this.isAnalyzing,
      activeReport: activeReport ?? this.activeReport,
      explanation: explanation ?? this.explanation,
      errorMessage: errorMessage,
    );
  }
}

class DiagnosisNotifier extends StateNotifier<DiagnosisState> {
  final FrontendDiagnosisService _service;

  DiagnosisNotifier(this._service) : super(const DiagnosisState(isAnalyzing: false));

  Future<bool> submitForDiagnosis({
    required String studentId,
    required String questionId,
    required dynamic answer,
    int timeSpentSeconds = 60,
    int hintsUsed = 0,
  }) async {
    state = state.copyWith(isAnalyzing: true);
    try {
      final res = await _service.analyzeSubmission(
        studentId: studentId,
        questionId: questionId,
        answer: answer,
        timeSpentSeconds: timeSpentSeconds,
        hintsUsed: hintsUsed,
      );
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(isAnalyzing: false, activeReport: res['data'] as Map<String, dynamic>);
        return true;
      } else {
        state = state.copyWith(isAnalyzing: false, errorMessage: res['message']);
        return false;
      }
    } catch (e) {
      state = state.copyWith(isAnalyzing: false, errorMessage: e.toString());
      return false;
    }
  }

  Future<void> fetchExplanation(String diagnosisId) async {
    try {
      final res = await _service.explainDiagnosis(diagnosisId);
      if (res['success'] == true) {
        state = state.copyWith(explanation: res['data'] as Map<String, dynamic>);
      }
    } catch (_) {}
  }
}

final diagnosisProvider = StateNotifierProvider<DiagnosisNotifier, DiagnosisState>((ref) {
  final service = ref.watch(frontendDiagnosisServiceProvider);
  return DiagnosisNotifier(service);
});
