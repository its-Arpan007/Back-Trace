import 'package:backtrace/core/network/api_client.dart';
import 'package:backtrace/core/constants/api_constants.dart';

class AuthService {
  final ApiClient _apiClient;

  AuthService(this._apiClient);

  Future<Map<String, dynamic>> register(Map<String, dynamic> data) async {
    final response = await _apiClient.post('/auth/register', data: data);
    return response as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> login(String usernameOrEmail, String password, {bool rememberMe = false}) async {
    final response = await _apiClient.post(
      '/auth/login',
      data: {
        'username_or_email': usernameOrEmail,
        'password': password,
        'remember_me': rememberMe,
        'device_info': 'Flutter Mobile/Web App',
      },
    );
    return response as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> refreshToken(String refreshToken) async {
    final response = await _apiClient.post(
      '/auth/refresh',
      data: {'refresh_token': refreshToken},
    );
    return response as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getMe() async {
    final response = await _apiClient.get('/auth/me');
    return response as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> logout() async {
    final response = await _apiClient.post('/auth/logout');
    return response as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> forgotPassword(String email) async {
    final response = await _apiClient.post(
      '/auth/forgot-password',
      data: {'email': email},
    );
    return response as Map<String, dynamic>;
  }
}
