import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/question/presentation/controllers/question_controller.dart';

class QuestionExplorerScreen extends ConsumerWidget {
  const QuestionExplorerScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(questionListProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Question Intelligence Bank'),
        actions: [
          IconButton(
            icon: const Icon(Icons.auto_awesome_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/adaptive-practice-generator'),
          ),
          IconButton(
            icon: const Icon(Icons.search_rounded),
            onPressed: () => context.push('/question-search'),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => context.push('/question-editor'),
        backgroundColor: AppColors.accentTeal,
        icon: const Icon(Icons.add_rounded, color: Colors.white),
        label: const Text('New Intelligence Question', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
      ),
      body: state.isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.accentTeal))
          : ListView(
              padding: const EdgeInsets.all(24),
              children: [
                Text(
                  'Educational Intelligence Objects',
                  style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white),
                ),
                const SizedBox(height: 8),
                Text(
                  'Questions structured to measure concept mastery, misconception codes, and root cause diagnosis.',
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(color: AppColors.textSecondaryDark),
                ),
                const SizedBox(height: 24),
                _buildQuestionCard(context, 'q1_arrays_01', 'Array Index Offset Calculation', 'MCQ', 'DSA_ARRAYS_01', 'Apply', 'Medium'),
                const SizedBox(height: 16),
                _buildQuestionCard(context, 'q2_trees_01', 'Binary Tree In-Order Traversal', 'Code', 'DSA_TREES_01', 'Apply', 'Hard'),
                const SizedBox(height: 16),
                _buildQuestionCard(context, 'q3_hash_01', 'Hash Collision Resolution Probe', 'Multiple Select', 'DSA_HASH_01', 'Analyze', 'Hard'),
              ],
            ),
    );
  }

  Widget _buildQuestionCard(BuildContext context, String id, String title, String type, String concept, String bloom, String diff) {
    return AppCard(
      onTap: () => context.push('/question-details?id=$id'),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: AppColors.accentTeal.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
                child: Text(type, style: const TextStyle(color: AppColors.accentTeal, fontSize: 10, fontWeight: FontWeight.bold)),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: AppColors.accentIndigo.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
                child: Text(concept, style: const TextStyle(color: AppColors.accentCyan, fontSize: 10, fontWeight: FontWeight.bold)),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('Bloom: $bloom', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
              Text('Difficulty: $diff', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
            ],
          ),
        ],
      ),
    );
  }
}
