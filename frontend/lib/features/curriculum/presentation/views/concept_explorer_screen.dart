import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ConceptExplorerScreen extends StatelessWidget {
  const ConceptExplorerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Concept Explorer')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          _buildConceptCard(context, 'DSA_ARRAYS_01', 'Array In-Memory Layout & Indexing', 'Apply', '85% Mastery', 'Medium'),
          const SizedBox(height: 16),
          _buildConceptCard(context, 'DSA_HASH_01', 'Hash Function Collision Handling', 'Analyze', '80% Mastery', 'Hard'),
          const SizedBox(height: 16),
          _buildConceptCard(context, 'DSA_TREES_01', 'Binary Search Tree Traversal (DFS/BFS)', 'Apply', '90% Mastery', 'Medium'),
        ],
      ),
    );
  }

  Widget _buildConceptCard(BuildContext context, String code, String title, String bloom, String threshold, String diff) {
    return AppCard(
      onTap: () => context.push('/concept-details?code=$code'),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: AppColors.accentTeal.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
                child: Text(code, style: const TextStyle(color: AppColors.accentTeal, fontSize: 11, fontWeight: FontWeight.bold)),
              ),
              Text('Bloom: $bloom', style: const TextStyle(color: AppColors.accentCyan, fontSize: 11)),
            ],
          ),
          const SizedBox(height: 8),
          Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('Mastery: $threshold', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
              Text('Difficulty: $diff', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
            ],
          ),
        ],
      ),
    );
  }
}
