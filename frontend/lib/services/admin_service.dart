import 'package:backtrace/core/network/api_client.dart';

class FrontendAdminService {
  final ApiClient _apiClient;

  FrontendAdminService(this._apiClient);

  Future<Map<String, dynamic>> getDashboard() async {
    final res = await _apiClient.get('/admin/dashboard');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getUsers() async {
    final res = await _apiClient.get('/admin/users');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getSystemHealth() async {
    final res = await _apiClient.get('/admin/system-health');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getAiConfig() async {
    final res = await _apiClient.get('/admin/ai-config');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getAuditLogs() async {
    final res = await _apiClient.get('/admin/audit-logs');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> getApprovals() async {
    final res = await _apiClient.get('/admin/approvals');
    return res as Map<String, dynamic>;
  }

  Future<Map<String, dynamic>> triggerBackup() async {
    final res = await _apiClient.post('/admin/backups');
    return res as Map<String, dynamic>;
  }
}
