import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminKnowledgeGraphEditorScreen extends StatelessWidget {
  const AdminKnowledgeGraphEditorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Interactive Knowledge Graph Editor')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.account_tree_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Graph DAG Visualizer & Editor', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Nodes: 42 • Edges: 65 • Cycle Detection: Passed • Version: 1.4.0', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
