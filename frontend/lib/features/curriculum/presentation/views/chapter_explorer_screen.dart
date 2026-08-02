import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ChapterExplorerScreen extends StatelessWidget {
  const ChapterExplorerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Chapter Explorer')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          _buildChapterItem(context, 'Chapter 1: Linear Data Structures', 'Arrays, Linked Lists, Stacks, Queues', 1, '12.0 hrs'),
          const SizedBox(height: 16),
          _buildChapterItem(context, 'Chapter 2: Tree Data Structures', 'Binary Trees, BST, AVL Trees, Heaps', 2, '18.0 hrs'),
          const SizedBox(height: 16),
          _buildChapterItem(context, 'Chapter 3: Graph Algorithms', 'DFS, BFS, Dijkstra, Topological Sort', 3, '24.0 hrs'),
        ],
      ),
    );
  }

  Widget _buildChapterItem(BuildContext context, String title, String desc, int order, String hours) {
    return AppCard(
      onTap: () => context.push('/topics-explorer'),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: AppColors.accentTeal,
          child: Text('$order', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        ),
        title: Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        subtitle: Text(desc, style: const TextStyle(color: AppColors.textSecondaryDark)),
        trailing: Text(hours, style: const TextStyle(color: AppColors.accentCyan, fontSize: 12)),
      ),
    );
  }
}
