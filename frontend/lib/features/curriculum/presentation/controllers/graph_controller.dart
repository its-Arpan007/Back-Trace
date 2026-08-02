import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/features/curriculum/presentation/controllers/curriculum_controller.dart';
import 'package:backtrace/services/curriculum_service.dart';

class GraphState {
  final bool isLoading;
  final Map<String, dynamic>? graphData;
  final Map<String, dynamic>? selectedConceptDeps;
  final String? errorMessage;

  const GraphState({required this.isLoading, this.graphData, this.selectedConceptDeps, this.errorMessage});

  GraphState copyWith({
    bool? isLoading,
    Map<String, dynamic>? graphData,
    Map<String, dynamic>? selectedConceptDeps,
    String? errorMessage,
  }) {
    return GraphState(
      isLoading: isLoading ?? this.isLoading,
      graphData: graphData ?? this.graphData,
      selectedConceptDeps: selectedConceptDeps ?? this.selectedConceptDeps,
      errorMessage: errorMessage,
    );
  }
}

class GraphNotifier extends StateNotifier<GraphState> {
  final FrontendCurriculumService _service;

  GraphNotifier(this._service) : super(const GraphState(isLoading: false)) {
    loadGraph();
  }

  Future<void> loadGraph() async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getGraph();
      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(isLoading: false, graphData: res['data'] as Map<String, dynamic>);
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }

  Future<void> selectConcept(String conceptCode) async {
    try {
      final res = await _service.getLearningPath(conceptCode);
      if (res['success'] == true) {
        state = state.copyWith(selectedConceptDeps: res['data'] as Map<String, dynamic>);
      }
    } catch (_) {}
  }
}

final graphProvider = StateNotifierProvider<GraphNotifier, GraphState>((ref) {
  final service = ref.watch(frontendCurriculumServiceProvider);
  return GraphNotifier(service);
});
