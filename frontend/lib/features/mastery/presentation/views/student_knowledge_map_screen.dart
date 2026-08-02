import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/mastery/presentation/controllers/mastery_controller.dart';

class StudentKnowledgeMapScreen extends ConsumerWidget {
  const StudentKnowledgeMapScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(masteryProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Student Knowledge Map & SLM'),
        actions: [
          IconButton(
            icon: const Icon(Icons.speed_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/learning-velocity'),
          ),
          IconButton(
            icon: const Icon(Icons.timer_outlined),
            onPressed: () => context.push('/retention-dashboard'),
          ),
        ],
      ),
      body: state.isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.accentTeal))
          : SingleChildScrollView(
              padding: const EdgeInsets.all(24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      StatusBadge(label: 'SLM DIGITAL TWIN ACTIVE', isOnline: true),
                      const Text('Overall Mastery: 78.5%', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 13)),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Text('Concept Knowledge Heatmap', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
                  const SizedBox(height: 8),
                  const Text('Continuously updated BKT knowledge state across your dynamic learning graph.', style: TextStyle(color: AppColors.textSecondaryDark)),
                  const SizedBox(height: 24),

                  // Heatmap Cards
                  _buildConceptHeatmapTile(context, 'DSA_ARRAYS_01', 'Array In-Memory Layout & Indexing', 0.88, 'Improving'),
                  const SizedBox(height: 12),
                  _buildConceptHeatmapTile(context, 'DSA_TREES_01', 'Binary Search Tree Traversals', 0.65, 'Plateau'),
                  const SizedBox(height: 12),
                  _buildConceptHeatmapTile(context, 'DSA_HASH_01', 'Hash Function Collision Handling', 0.72, 'Improving'),
                  const SizedBox(height: 12),
                  _buildConceptHeatmapTile(context, 'DSA_GRAPH_01', 'Graph Shortest Path & Topological Sort', 0.40, 'Regressing'),
                  const SizedBox(height: 24),

                  ElevatedButton.icon(
                    onPressed: () => context.push('/concept-timeline?concept=DSA_ARRAYS_01'),
                    icon: const Icon(Icons.timeline_rounded),
                    label: const Text('View Concept Learning Progression Timeline'),
                    style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(double.infinity, 50)),
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildConceptHeatmapTile(BuildContext context, String code, String title, floatScore, String trend) {
    final pct = (floatScore * 100).toInt();
    final color = floatScore >= 0.80
        ? AppColors.success
        : floatScore >= 0.60
            ? AppColors.warning
            : AppColors.error;

    return AppCard(
      onTap: () => context.push('/concept-timeline?concept=$code'),
      child: Row(
        children: [
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(color: color.withOpacity(0.2), borderRadius: BorderRadius.circular(12), border: Border.all(color: color)),
            child: Center(child: Text('$pct%', style: TextStyle(color: color, fontWeight: FontWeight.bold, fontSize: 13))),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(code, style: TextStyle(color: color, fontWeight: FontWeight.bold, fontSize: 11)),
                const SizedBox(height: 2),
                Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 14)),
                const SizedBox(height: 2),
                Text('Trend: $trend', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 11)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
