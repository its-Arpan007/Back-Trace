import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/interactive_graph.dart';
import 'package:backtrace/features/curriculum/presentation/controllers/graph_controller.dart';

class KnowledgeGraphViewerScreen extends ConsumerWidget {
  const KnowledgeGraphViewerScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final graphState = ref.watch(graphProvider);

    final mockNodes = [
      GraphNodeData(id: 'DSA_ARRAYS_01', label: 'Arrays & Memory', domain: 'DSA', position: const Offset(150, 150), isHighlighted: true),
      GraphNodeData(id: 'DSA_HASH_01', label: 'Hash Tables', domain: 'DSA', position: const Offset(400, 100)),
      GraphNodeData(id: 'DSA_TREES_01', label: 'Binary Trees', domain: 'DSA', position: const Offset(400, 250)),
      GraphNodeData(id: 'DSA_GRAPH_01', label: 'Graph Traversals', domain: 'DSA', position: const Offset(650, 180), isTarget: true),
    ];

    final mockEdges = [
      GraphEdgeData(sourceId: 'DSA_ARRAYS_01', targetId: 'DSA_HASH_01'),
      GraphEdgeData(sourceId: 'DSA_ARRAYS_01', targetId: 'DSA_TREES_01'),
      GraphEdgeData(sourceId: 'DSA_HASH_01', targetId: 'DSA_GRAPH_01'),
      GraphEdgeData(sourceId: 'DSA_TREES_01', targetId: 'DSA_GRAPH_01'),
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('DAG Knowledge Graph Visualizer'),
        actions: [
          IconButton(
            icon: const Icon(Icons.fact_check_outlined, color: AppColors.accentTeal),
            onPressed: () => context.push('/graph-validation-report'),
          ),
          IconButton(
            icon: const Icon(Icons.file_upload_outlined),
            onPressed: () => context.push('/curriculum-import-status'),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Expanded(
              child: InteractiveKnowledgeGraphWidget(
                nodes: mockNodes,
                edges: mockEdges,
                onNodeSelected: (node) {
                  ref.read(graphProvider.notifier).selectConcept(node.id);
                },
              ),
            ),
            const SizedBox(height: 12),
            if (graphState.selectedConceptDeps != null)
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: AppColors.darkCard, borderRadius: BorderRadius.circular(12)),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Selected Target: ${graphState.selectedConceptDeps?["target_concept"]}',
                      style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                    ),
                    ElevatedButton(
                      onPressed: () => context.push('/learning-path-viewer'),
                      style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal),
                      child: const Text('View Path'),
                    ),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }
}
