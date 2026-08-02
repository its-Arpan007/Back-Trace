import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/api_service.dart';

class SplashState {
  final bool isLoading;
  final bool isBackendConnected;
  final String statusMessage;

  const SplashState({
    required this.isLoading,
    required this.isBackendConnected,
    required this.statusMessage,
  });

  SplashState copyWith({
    bool? isLoading,
    bool? isBackendConnected,
    String? statusMessage,
  }) {
    return SplashState(
      isLoading: isLoading ?? this.isLoading,
      isBackendConnected: isBackendConnected ?? this.isBackendConnected,
      statusMessage: statusMessage ?? this.statusMessage,
    );
  }
}

class SplashNotifier extends StateNotifier<SplashState> {
  final ApiService _apiService;

  SplashNotifier(this._apiService)
      : super(const SplashState(
          isLoading: true,
          isBackendConnected: false,
          statusMessage: 'Initializing BACKTRACE Learning Engine...',
        )) {
    checkSystemStatus();
  }

  Future<void> checkSystemStatus() async {
    state = state.copyWith(
      isLoading: true,
      statusMessage: 'Connecting to BACKTRACE Backend API...',
    );

    try {
      final res = await _apiService.checkHealth();
      if (res['success'] == true) {
        state = state.copyWith(
          isLoading: false,
          isBackendConnected: true,
          statusMessage: 'BACKTRACE Diagnostics System Operational',
        );
      } else {
        state = state.copyWith(
          isLoading: false,
          isBackendConnected: false,
          statusMessage: 'Backend degraded or offline',
        );
      }
    } catch (e) {
      state = state.copyWith(
        isLoading: false,
        isBackendConnected: false,
        statusMessage: 'Standalone Mode (Backend Connection Pending)',
      );
    }
  }
}

final splashControllerProvider =
    StateNotifierProvider<SplashNotifier, SplashState>((ref) {
  final apiService = ref.watch(apiServiceProvider);
  return SplashNotifier(apiService);
});
