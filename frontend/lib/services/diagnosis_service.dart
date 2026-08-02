import 'package:backtrace/core/network/api_client.dart';

class FrontendDiagnosisService {
  final ApiClient _apiClient;

  FrontendDiagnosisService(this._apiClient);

  Future<Map<String, dynamic>> analyzeSubmission({
    required String studentId,
    required String questionId,
    required dynamic answer,
    int timeSpentSeconds = 60,
    int hintsUsed = 0,
  }) async {
    final res = await _apiClient.post(
      '/diagnosis/analyze',
      data: {
        'student_id': studentId,
        'question_id': questionId,
        'student_answer': answer,
        'time_spent_seconds': timeSpentSeconds,
        'hints_used': hintsUsed,
      },
    );
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getDiagnosisById(String diagnosisId) async {
    final res = await _apiClient.get('/diagnosis/$diagnosisId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getStudentHistory(String studentId) async {
    final res = await _apiClient.get('/diagnosis/student/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> explainDiagnosis(String diagnosisId) async {
    final res = await _apiClient.post('/diagnosis/explain', data: {'diagnosis_id': diagnosisId});
    return res as Map<String, dynamic>;
  }
}
