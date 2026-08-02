import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/assessment_builder/presentation/controllers/assessment_builder_controller.dart';

class AssessmentBuilderScreen extends ConsumerWidget {
  const AssessmentBuilderScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(assessmentBuilderProvider);
    final notifier = ref.read(assessmentBuilderProvider.notifier);

    return Scaffold(
      appBar: AppBar(title: const Text('Knowledge Graph Assessment Builder')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Build Assessment from Knowledge Graph', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Select target concept nodes, difficulty levels, and Bloom levels to auto-generate aligned quizzes.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          AppCard(
            child: TextField(
              decoration: const InputDecoration(labelText: 'Assessment Title', border: OutlineInputBorder()),
              onChanged: notifier.setTitle,
            ),
          ),
          const SizedBox(height: 24),

          ElevatedButton.icon(
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Assessment Generated from Knowledge Graph Nodes!')),
              );
            },
            icon: const Icon(Icons.auto_awesome_rounded),
            label: const Text('Generate Assessment'),
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(double.infinity, 50)),
          ),
        ],
      ),
    );
  }
}
