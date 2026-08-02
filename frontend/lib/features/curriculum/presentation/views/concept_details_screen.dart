import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ConceptDetailsScreen extends StatelessWidget {
  const ConceptDetailsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Concept Intelligence Details')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(color: AppColors.accentTeal.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
            child: const Text('CONCEPT CODE: DSA_ARRAYS_01', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold)),
          ),
          const SizedBox(height: 12),
          Text('Array In-Memory Layout & Indexing', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Contiguous memory locations mapped via pointer arithmetic formula: Address = Base + i * ElementSize.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          // Learning Objectives
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Learning Objectives', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                Divider(color: AppColors.darkBorder),
                Text('• Calculate offset address given base pointer and element stride.', style: TextStyle(color: AppColors.textSecondaryDark)),
                Text('• Analyze 0-based vs 1-based indexing tradeoffs in memory bounds.', style: TextStyle(color: AppColors.textSecondaryDark)),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Misconception Library
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Misconception Library', style: TextStyle(color: AppColors.warning, fontWeight: FontWeight.bold, fontSize: 16)),
                const Divider(color: AppColors.darkBorder),
                const Text('MIS_ARRAY_BOUNDS_01: Off-by-one indexing error accessing length index.', style: TextStyle(color: Colors.white, fontSize: 13)),
                const SizedBox(height: 4),
                const Text('Remediation: Interactive array bounds visualizer.', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
              ],
            ),
          ),
          const SizedBox(height: 24),
          ElevatedButton.icon(
            onPressed: () => context.push('/learning-path-viewer?concept=DSA_ARRAYS_01'),
            icon: const Icon(Icons.alt_route_rounded),
            label: const Text('View Prerequisite Learning Path'),
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.accentTeal,
              minimumSize: const Size(double.infinity, 50),
            ),
          ),
        ],
      ),
    );
  }
}
