import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/auth_service.dart';

class ProfileState {
  final bool isLoading;
  final Map<String, dynamic>? profileData;
  final String? errorMessage;

  const ProfileState({
    required this.isLoading,
    this.profileData,
    this.errorMessage,
  });

  ProfileState copyWith({
    bool? isLoading,
    Map<String, dynamic>? profileData,
    String? errorMessage,
  }) {
    return ProfileState(
      isLoading: isLoading ?? this.isLoading,
      profileData: profileData ?? this.profileData,
      errorMessage: errorMessage,
    );
  }
}

class ProfileNotifier extends StateNotifier<ProfileState> {
  final AuthService _authService;

  ProfileNotifier(this._authService) : super(const ProfileState(isLoading: false));

  Future<void> fetchProfile() async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _authService.getMe();
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(
          isLoading: false,
          profileData: res['data'] as Map<String, dynamic>,
        );
      } else {
        state = state.copyWith(
          isLoading: false,
          errorMessage: res['message'] ?? 'Failed to fetch profile',
        );
      }
    } catch (e) {
      state = state.copyWith(
        isLoading: false,
        errorMessage: e.toString(),
      );
    }
  }
}

final profileProvider = StateNotifierProvider<ProfileNotifier, ProfileState>((ref) {
  final authService = ref.watch(authServiceProvider);
  return ProfileNotifier(authService);
});
