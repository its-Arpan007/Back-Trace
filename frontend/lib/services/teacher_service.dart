import 'package:backtrace/core/network/api_client.dart';

class FrontendTeacherService {
  final ApiClient _apiClient;

  FrontendTeacherService(this._apiClient);

  Future<Map<String, dynamic>> getTeacherClasses() async {
    final res = await _apiClient.get('/teacher/classes');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getClassAnalytics(String classId) async {
    final res = await _apiClient.get('/teacher/classes/$classId/analytics');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getInterventions() async {
    final res = await _apiClient.get('/teacher/interventions');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> buildAssessment(Map<String, dynamic> reqBody) async {
    final res = await _apiClient.post('/teacher/assessments', data: reqBody);
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> createAssignment(Map<String, dynamic> reqBody) async {
    final res = await _apiClient.post('/teacher/assignments', data: reqBody);
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getReports() async {
    final res = await _apiClient.get('/teacher/reports');
    return res as Map<String, dynamic>;
  }
}
