import 'package:backtrace/core/network/api_client.dart';

class FrontendRecommendationService {
  final ApiClient _apiClient;

  FrontendRecommendationService(this._apiClient);

  Future<Map<String, dynamic>> getStudentRecommendations(String studentId) async {
    final res = await _apiClient.get('/recommendations/student/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getTodaysPlan(String studentId) async {
    final res = await _apiClient.get('/recommendations/today/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getWeeklyPlan(String studentId) async {
    final res = await _apiClient.get('/recommendations/weekly/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getRevisionSchedule(String studentId) async {
    final res = await _apiClient.get('/recommendations/revision/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getRecommendedResources(String studentId) async {
    final res = await _apiClient.get('/recommendations/resources/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getRecommendedQuestions(String studentId) async {
    final res = await _apiClient.get('/recommendations/questions/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> submitFeedback({
    required String studentId,
    required String recommendationId,
    int rating = 5,
    String? feedbackText,
    String actionTaken = 'accepted',
  }) async {
    final res = await _apiClient.post('/recommendations/feedback', data: {
      'student_id': studentId,
      'recommendation_id': recommendationId,
      'rating_score': rating,
      'feedback_text': feedbackText,
      'action_taken': actionTaken,
    });
    return res as Map<String, dynamic>;
  }
}
