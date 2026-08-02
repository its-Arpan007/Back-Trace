import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/shared/widgets/custom_button.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/question/presentation/controllers/adaptive_question_controller.dart';

class AdaptivePracticeGeneratorScreen extends ConsumerStatefulWidget {
  const AdaptivePracticeGeneratorScreen({super.key});

  @override
  ConsumerState<AdaptivePracticeGeneratorScreen> createState() => _AdaptivePracticeGeneratorScreenState();
}

class _AdaptivePracticeGeneratorScreenState extends ConsumerState<AdaptivePracticeGeneratorScreen> {
  String _selectedDifficulty = "medium";
  int _questionCount = 5;

  void _handleGenerate() async {
    await ref.read(adaptivePracticeProvider.notifier).generateSet(['DSA_ARRAYS_01', 'DSA_TREES_01'], _selectedDifficulty, _questionCount);
  }

  @override
  Widget build(BuildContext context) {
    final state = ref.watch(adaptivePracticeProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('Adaptive Practice Set Generator')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Personalized Assessment Engine', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Generates adaptive question sets targeting your specific prerequisite gaps and concept weaknesses.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          // Difficulty Selector
          Container(
            decoration: BoxDecoration(color: AppColors.darkCard, borderRadius: BorderRadius.circular(12)),
            child: Row(
              children: ['easy', 'medium', 'hard'].map((diff) {
                final isSel = _selectedDifficulty == diff;
                return Expanded(
                  child: GestureDetector(
                    onTap: () => setState(() => _selectedDifficulty = diff),
                    child: Container(
                      padding: const EdgeInsets.vertical(12),
                      decoration: BoxDecoration(
                        color: isSel ? AppColors.accentTeal : Colors.transparent,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(diff.toUpperCase(), textAlign: TextAlign.center, style: TextStyle(color: isSel ? Colors.white : AppColors.textSecondaryDark, fontWeight: FontWeight.bold, fontSize: 12)),
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
          const SizedBox(height: 24),

          SizedBox(
            width: double.infinity,
            child: CustomButton(
              label: 'Generate Adaptive Practice Set',
              isLoading: state.isLoading,
              onPressed: _handleGenerate,
              icon: Icons.auto_awesome_rounded,
            ),
          ),
          const SizedBox(height: 24),

          if (state.practiceSet != null)
            AppCard(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text('Generated Adaptive Set', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                  const Divider(color: AppColors.darkBorder),
                  Text('Set ID: ${state.practiceSet?["practice_set_id"]}', style: const TextStyle(color: AppColors.accentCyan, fontSize: 13)),
                  Text('Target Concepts: ${state.practiceSet?["concept_codes"]}', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                  const SizedBox(height: 12),
                  ElevatedButton(
                    onPressed: () => context.push('/question-preview'),
                    style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal),
                    child: const Text('Start Adaptive Assessment Session'),
                  ),
                ],
              ),
            ),
        ],
      ),
    );
  }
}
