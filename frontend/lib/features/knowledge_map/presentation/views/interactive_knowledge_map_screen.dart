import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/knowledge_map/presentation/controllers/knowledge_map_controller.dart';

class InteractiveKnowledgeMapScreen extends ConsumerWidget {
  const InteractiveKnowledgeMapScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(knowledgeMapProvider);
    final notifier = ref.read(knowledgeMapProvider.notifier);

    final graphNodes = [
      {'code': 'DSA_COMPARISONS_01', 'title': 'Comparison Operators', 'status': 'Mastered (100%)', 'color': AppColors.success},
      {'code': 'DSA_ARRAYS_01', 'title': 'Array Memory Layout & Stride', 'status': 'In Remediation (65%)', 'color': AppColors.warning},
      {'code': 'DSA_SORTED_ARRAYS_01', 'title': 'Sorted Arrays', 'status': 'Locked Node', 'color': AppColors.textSecondaryDark},
      {'code': 'DSA_BINARY_SEARCH_01', 'title': 'Binary Search', 'status': 'Target Goal', 'color': AppColors.accentTeal},
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Interactive Knowledge DAG Map')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Personalized Cognitive Knowledge DAG', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Tap any concept node to inspect prerequisites, mastery state, and diagnostic attempt history.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          ...graphNodes.map((n) {
            final isSel = state.selectedConcept == n['code'];
            return Padding(
              padding: const EdgeInsets.only(bottom: 12.0),
              child: AppCard(
                onTap: () {
                  notifier.selectConcept(n['code'] as String);
                  context.push('/concept-details');
                },
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: (n['color'] as Color).withOpacity(0.2),
                    child: Icon(Icons.hub_rounded, color: n['color'] as Color, size: 20),
                  ),
                  title: Text(n['title'] as String, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  subtitle: Text('Code: ${n['code']} • ${n['status']}', style: TextStyle(color: n['color'] as Color, fontSize: 12)),
                  trailing: const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textSecondaryDark, size: 14),
                ),
              ),
            );
          }).toList(),
        ],
      ),
    );
  }
}
