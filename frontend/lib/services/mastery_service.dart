import 'package:backtrace/core/network/api_client.dart';

class FrontendMasteryService {
  final ApiClient _apiClient;

  FrontendMasteryService(this._apiClient);

  Future<Map<String, dynamic>> getStudentMasterySummary(String studentId) async {
    final res = await _apiClient.get('/mastery/student/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getConceptMastery(String studentId, String conceptCode) async {
    final res = await _apiClient.get('/mastery/concept/$studentId/$conceptCode');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getLearningTimeline(String studentId, {String conceptCode = 'DSA_ARRAYS_01'}) async {
    final res = await _apiClient.get('/mastery/timeline/$studentId', queryParameters: {'concept_code': conceptCode});
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getMasteryPredictions(String studentId) async {
    final res = await _apiClient.get('/mastery/predictions/$studentId');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getStudentStatistics(String studentId) async {
    final res = await _apiClient.get('/mastery/statistics/$studentId');
    return res as Map<String, dynamic>;
  }
}
