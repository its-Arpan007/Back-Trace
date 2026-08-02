import 'package:backtrace/core/network/api_client.dart';

class FrontendAIService {
  final ApiClient _apiClient;

  FrontendAIService(this._apiClient);

  Future<Map<String, dynamic>> sendChatMessage(String userId, String message, {String? conceptCode, String provider = 'gemini'}) async {
    final res = await _apiClient.post('/ai/chat', data: {
      'user_id': userId,
      'message': message,
      'concept_code': conceptCode,
      'provider': provider,
    });
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> explainConcept(String conceptCode, {String type = 'analogy'}) async {
    final res = await _apiClient.post('/ai/explain', data: {
      'concept_code': conceptCode,
      'explanation_type': type,
    });
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> generateStudyPlan(String studentId, String targetDate) async {
    final res = await _apiClient.post('/ai/study-plan', data: {
      'student_id': studentId,
      'target_date': targetDate,
    });
    return res as Map<String, dynamic>;
  }
}
