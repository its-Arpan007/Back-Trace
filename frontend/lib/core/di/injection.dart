import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/network/dio_client.dart';
import 'package:backtrace/core/network/api_client.dart';
import 'package:backtrace/services/api_service.dart';
import 'package:backtrace/services/storage_service.dart';
import 'package:backtrace/services/secure_storage_service.dart';
import 'package:backtrace/services/auth_service.dart';

final dioClientProvider = Provider<DioClient>((ref) {
  return DioClient();
});

final apiClientProvider = Provider<ApiClient>((ref) {
  final dioClient = ref.watch(dioClientProvider);
  return ApiClient(dioClient);
});

final apiServiceProvider = Provider<ApiService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return ApiService(apiClient);
});

final authServiceProvider = Provider<AuthService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return AuthService(apiClient);
});

final storageServiceProvider = Provider<StorageService>((ref) {
  return InMemoryStorageService();
});

final secureStorageServiceProvider = Provider<SecureStorageService>((ref) {
  return InMemorySecureStorageService();
});
