import 'package:backtrace/core/network/api_client.dart';

class FrontendQuestionService {
  final ApiClient _apiClient;

  FrontendQuestionService(this._apiClient);

  Future<Map<String, dynamic>> getQuestions() async {
    final res = await _apiClient.get('/questions');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getQuestionById(String id) async {
    final res = await _apiClient.get('/questions/$id');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> searchQuestions(String query) async {
    final res = await _apiClient.get('/questions/search', queryParameters: {'q': query});
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> generatePracticeSet(Map<String, dynamic> reqData) async {
    final res = await _apiClient.post('/questions/practice-set', data: reqData);
    return res as Map<String, dynamic>;
  }
}
