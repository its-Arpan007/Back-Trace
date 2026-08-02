import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/auth_service.dart';
import 'package:backtrace/services/secure_storage_service.dart';

enum AuthStatus { unauthenticated, authenticating, authenticated, error }

class AuthState {
  final AuthStatus status;
  final String? userId;
  final String? role;
  final String? errorMessage;

  const AuthState({
    required this.status,
    this.userId,
    this.role,
    this.errorMessage,
  });

  AuthState copyWith({
    AuthStatus? status,
    String? userId,
    String? role,
    String? errorMessage,
  }) {
    return AuthState(
      status: status ?? this.status,
      userId: userId ?? this.userId,
      role: role ?? this.role,
      errorMessage: errorMessage,
    );
  }
}

class AuthNotifier extends StateNotifier<AuthState> {
  final AuthService _authService;
  final SecureStorageService _secureStorage;
  final Ref _ref;

  AuthNotifier(this._authService, this._secureStorage, this._ref)
      : super(const AuthState(status: AuthStatus.unauthenticated)) {
    _checkInitialAuth();
  }

  Future<void> _checkInitialAuth() async {
    final token = await _secureStorage.read(SecureStorageKeys.accessToken);
    final userRole = await _secureStorage.read(SecureStorageKeys.userRole);
    final userId = await _secureStorage.read(SecureStorageKeys.userId);

    if (token != null && token.isNotEmpty) {
      _ref.read(dioClientProvider).authInterceptor.setToken(token);
      state = state.copyWith(
        status: AuthStatus.authenticated,
        userId: userId,
        role: userRole,
      );
    } else {
      state = state.copyWith(status: AuthStatus.unauthenticated);
    }
  }

  Future<bool> login(String usernameOrEmail, String password, {bool rememberMe = false}) async {
    state = state.copyWith(status: AuthStatus.authenticating);
    try {
      final res = await _authService.login(usernameOrEmail, password, rememberMe: rememberMe);
      if (res['success'] == true && res['data'] != null) {
        final data = res['data'];
        final accessToken = data['access_token'] as String;
        final refreshToken = data['refresh_token'] as String;
        final role = data['role'] as String;
        final userId = data['user_id'] as String;
        final sessionId = data['session_id'] as String;

        await _secureStorage.write(SecureStorageKeys.accessToken, accessToken);
        await _secureStorage.write(SecureStorageKeys.refreshToken, refreshToken);
        await _secureStorage.write(SecureStorageKeys.userRole, role);
        await _secureStorage.write(SecureStorageKeys.userId, userId);
        await _secureStorage.write(SecureStorageKeys.sessionId, sessionId);

        _ref.read(dioClientProvider).authInterceptor.setToken(accessToken);

        state = state.copyWith(
          status: AuthStatus.authenticated,
          userId: userId,
          role: role,
        );
        return true;
      } else {
        state = state.copyWith(
          status: AuthStatus.error,
          errorMessage: res['message'] ?? 'Login failed',
        );
        return false;
      }
    } catch (e) {
      state = state.copyWith(
        status: AuthStatus.error,
        errorMessage: e.toString(),
      );
      return false;
    }
  }

  Future<bool> register(Map<String, dynamic> reqData) async {
    state = state.copyWith(status: AuthStatus.authenticating);
    try {
      final res = await _authService.register(reqData);
      if (res['success'] == true) {
        state = state.copyWith(status: AuthStatus.unauthenticated);
        return true;
      } else {
        state = state.copyWith(
          status: AuthStatus.error,
          errorMessage: res['message'] ?? 'Registration failed',
        );
        return false;
      }
    } catch (e) {
      state = state.copyWith(
        status: AuthStatus.error,
        errorMessage: e.toString(),
      );
      return false;
    }
  }

  Future<void> logout() async {
    try {
      await _authService.logout();
    } catch (_) {}
    await _secureStorage.clearAll();
    _ref.read(dioClientProvider).authInterceptor.setToken(null);
    state = const AuthState(status: AuthStatus.unauthenticated);
  }
}

final authProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
  final authService = ref.watch(authServiceProvider);
  final secureStorage = ref.watch(secureStorageServiceProvider);
  return AuthNotifier(authService, secureStorage, ref);
});

final currentUserRoleProvider = Provider<String?>((ref) {
  return ref.watch(authProvider).role;
});
