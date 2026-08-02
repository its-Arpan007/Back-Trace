import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/recommendation_service.dart';

final frontendRecommendationServiceProvider = Provider<FrontendRecommendationService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendRecommendationService(apiClient);
});

class RecommendationState {
  final bool isLoading;
  final List<dynamic>? recommendations;
  final Map<String, dynamic>? todaysPlan;
  final Map<String, dynamic>? weeklyPlan;
  final String? errorMessage;

  const RecommendationState({
    required this.isLoading,
    this.recommendations,
    this.todaysPlan,
    this.weeklyPlan,
    this.errorMessage,
  });

  RecommendationState copyWith({
    bool? isLoading,
    List<dynamic>? recommendations,
    Map<String, dynamic>? todaysPlan,
    Map<String, dynamic>? weeklyPlan,
    String? errorMessage,
  }) {
    return RecommendationState(
      isLoading: isLoading ?? this.isLoading,
      recommendations: recommendations ?? this.recommendations,
      todaysPlan: todaysPlan ?? this.todaysPlan,
      weeklyPlan: weeklyPlan ?? this.weeklyPlan,
      errorMessage: errorMessage,
    );
  }
}

class RecommendationNotifier extends StateNotifier<RecommendationState> {
  final FrontendRecommendationService _service;

  RecommendationNotifier(this._service) : super(const RecommendationState(isLoading: false)) {
    loadRecommendations("11111111-1111-1111-1111-111111111111");
  }

  Future<void> loadRecommendations(String studentId) async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getStudentRecommendations(studentId);
      final planRes = await _service.getTodaysPlan(studentId);
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(
          isLoading: false,
          recommendations: res['data'] as List<dynamic>,
          todaysPlan: planRes['data'] as Map<String, dynamic>?,
        );
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }

  Future<void> submitFeedback(String recId, int rating) async {
    try {
      await _service.submitFeedback(
        studentId: "11111111-1111-1111-1111-111111111111",
        recommendationId: recId,
        rating: rating,
      );
    } catch (_) {}
  }
}

final recommendationProvider = StateNotifierProvider<RecommendationNotifier, RecommendationState>((ref) {
  final service = ref.watch(frontendRecommendationServiceProvider);
  return RecommendationNotifier(service);
});
