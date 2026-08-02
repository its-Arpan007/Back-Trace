import 'package:flutter_riverpod/flutter_riverpod.dart';

class ClassState {
  final String selectedClassId;
  final bool isLoading;

  const ClassState({
    this.selectedClassId = "c_dsa_101",
    this.isLoading = false,
  });

  ClassState copyWith({String? selectedClassId, bool? isLoading}) {
    return ClassState(
      selectedClassId: selectedClassId ?? this.selectedClassId,
      isLoading: isLoading ?? this.isLoading,
    );
  }
}

class ClassNotifier extends StateNotifier<ClassState> {
  ClassNotifier() : super(const ClassState());

  void selectClass(String classId) => state = state.copyWith(selectedClassId: classId);
}

final classProvider = StateNotifierProvider<ClassNotifier, ClassState>((ref) {
  return ClassNotifier();
});
