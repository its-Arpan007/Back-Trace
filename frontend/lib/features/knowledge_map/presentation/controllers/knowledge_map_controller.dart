import 'package:flutter_riverpod/flutter_riverpod.dart';

class KnowledgeMapState {
  final String selectedConcept;
  final bool isLoading;

  const KnowledgeMapState({
    this.selectedConcept = "DSA_ARRAYS_01",
    this.isLoading = false,
  });

  KnowledgeMapState copyWith({String? selectedConcept, bool? isLoading}) {
    return KnowledgeMapState(
      selectedConcept: selectedConcept ?? this.selectedConcept,
      isLoading: isLoading ?? this.isLoading,
    );
  }
}

class KnowledgeMapNotifier extends StateNotifier<KnowledgeMapState> {
  KnowledgeMapNotifier() : super(const KnowledgeMapState());

  void selectConcept(String code) => state = state.copyWith(selectedConcept: code);
}

final knowledgeMapProvider = StateNotifierProvider<KnowledgeMapNotifier, KnowledgeMapState>((ref) {
  return KnowledgeMapNotifier();
});
