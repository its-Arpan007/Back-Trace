import 'package:backtrace/core/network/api_client.dart';
import 'package:backtrace/core/constants/api_constants.dart';

class ApiService {
  final ApiClient _apiClient;

  ApiService(this._apiClient);

  Future<Map<String, dynamic>> checkHealth() async {
    final response = await _apiClient.get(ApiConstants.healthEndpoint);
    return response as Map<String, dynamic>;
  }
}
