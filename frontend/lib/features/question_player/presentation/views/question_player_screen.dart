import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/shared/widgets/custom_button.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/question_player/presentation/controllers/question_player_controller.dart';
import 'package:backtrace/features/diagnosis/presentation/controllers/diagnosis_controller.dart';

class QuestionPlayerScreen extends ConsumerStatefulWidget {
  const QuestionPlayerScreen({super.key});

  @override
  ConsumerState<QuestionPlayerScreen> createState() => _QuestionPlayerScreenState();
}

class _QuestionPlayerScreenState extends ConsumerState<QuestionPlayerScreen> {
  final _textController = TextEditingController(text: "0x1005");

  void _handleSubmit() async {
    final state = ref.read(questionPlayerProvider);
    final success = await ref.read(diagnosisProvider.notifier).submitForDiagnosis(
          studentId: "11111111-1111-1111-1111-111111111111",
          questionId: "q1_arrays_01",
          answer: _textController.text.trim(),
          timeSpentSeconds: state.timeSpentSeconds,
          hintsUsed: state.hintUnlocked ? 1 : 0,
        );

    if (mounted && success) {
      context.push('/reflection');
    }
  }

  @override
  Widget build(BuildContext context) {
    final playerState = ref.watch(questionPlayerProvider);
    final diagState = ref.watch(diagnosisProvider);
    final notifier = ref.read(questionPlayerProvider.notifier);

    return Scaffold(
      appBar: AppBar(
        title: Text('Question ${playerState.currentQuestionIndex + 1} of ${playerState.totalQuestions}'),
        actions: [
          IconButton(
            icon: Icon(playerState.isBookmarked ? Icons.bookmark_rounded : Icons.bookmark_border_rounded, color: AppColors.accentTeal),
            onPressed: notifier.toggleBookmark,
          ),
          IconButton(
            icon: const Icon(Icons.lightbulb_outline_rounded, color: AppColors.warning),
            onPressed: notifier.unlockHint,
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          // Question Statement Header
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('CONCEPT: DSA_ARRAYS_01 • BLOOM: APPLY', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 11)),
                SizedBox(height: 8),
                Text('Given base address 0x1000 and element size 4 bytes, calculate the memory address of array element at index 5.', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Unlocked Hint Card
          if (playerState.hintUnlocked)
            AppCard(
              child: ListTile(
                leading: const Icon(Icons.lightbulb_rounded, color: AppColors.warning),
                title: const Text('Hint Level 1', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: const Text('Remember the stride formula: Address = Base + (Index * Stride)', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          const SizedBox(height: 16),

          // Answer Input TextField
          TextField(
            controller: _textController,
            decoration: InputDecoration(
              labelText: 'Your Solution / Code Output',
              filled: true,
              fillColor: AppColors.darkCard,
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
          ),
          const SizedBox(height: 24),

          // Self-Reported Confidence Rating (1-5)
          const Text('How confident are you in this answer?', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 13)),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: List.generate(5, (idx) {
              final val = idx + 1;
              final isSel = playerState.confidenceScore == val;
              return ChoiceChip(
                label: Text('$val'),
                selected: isSel,
                selectedColor: AppColors.accentTeal,
                onSelected: (_) => notifier.setConfidence(val),
              );
            }),
          ),
          const SizedBox(height: 32),

          // Action Buttons
          SizedBox(
            width: double.infinity,
            child: CustomButton(
              label: 'Submit Answer for Diagnosis',
              isLoading: diagState.isAnalyzing,
              onPressed: _handleSubmit,
              icon: Icons.send_rounded,
            ),
          ),
        ],
      ),
    );
  }
}
