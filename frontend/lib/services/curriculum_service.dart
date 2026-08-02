import 'package:backtrace/core/network/api_client.dart';

class FrontendCurriculumService {
  final ApiClient _apiClient;

  FrontendCurriculumService(this._apiClient);

  Future<Map<String, dynamic>> getSubjects() async {
    final res = await _apiClient.get('/subjects');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getChapters(String subjectId) async {
    final res = await _apiClient.get('/chapters', queryParameters: {'subject_id': subjectId});
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getTopics(String chapterId) async {
    final res = await _apiClient.get('/topics', queryParameters: {'chapter_id': chapterId});
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getConcepts(String topicId) async {
    final res = await _apiClient.get('/concepts', queryParameters: {'topic_id': topicId});
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getGraph() async {
    final res = await _apiClient.get('/graph');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getLearningPath(String conceptCode) async {
    final res = await _apiClient.get('/graph/learning-path/$conceptCode');
    return res as Map<String, dynamic>;
  }
}
