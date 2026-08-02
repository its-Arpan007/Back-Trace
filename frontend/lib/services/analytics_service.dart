import 'package:backtrace/core/network/api_client.dart';

class FrontendAnalyticsService {
  final ApiClient _apiClient;

  FrontendAnalyticsService(this._apiClient);

  Future<Map<String, dynamic>> getStudentAnalytics(String studentId) async {
    final res = await _apiClient.get('/analytics/student/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getTeacherAnalytics(String teacherId) async {
    final res = await _apiClient.get('/analytics/teacher/$teacherId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getInstitutionAnalytics(String institutionId) async {
    final res = await _apiClient.get('/analytics/institution/$institutionId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getConceptAnalytics() async {
    final res = await _apiClient.get('/analytics/concepts');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getQuestionAnalytics() async {
    final res = await _apiClient.get('/analytics/questions');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getPredictions(String studentId) async {
    final res = await _apiClient.get('/analytics/predictions/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getReports(String studentId) async {
    final res = await _apiClient.get('/analytics/reports/$studentId');
    return res as Map<String, dynamic>;
  }
}
