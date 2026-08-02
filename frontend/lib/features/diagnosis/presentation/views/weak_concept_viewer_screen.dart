import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class WeakConceptViewerScreen extends StatelessWidget {
  const WeakConceptViewerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Weak Concept & Broken Chain Analysis')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.account_tree_outlined, color: AppColors.warning),
              title: Text('Upstream Prerequisite: DSA_ARRAYS_01', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Status: Weak / Unmastered • Causing downstream failures in DSA_TREES_01 and DSA_GRAPH_01', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
