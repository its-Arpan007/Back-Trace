import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionDetailsScreen extends StatelessWidget {
  const QuestionDetailsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Question Intelligence Object'),
        actions: [
          IconButton(
            icon: const Icon(Icons.bar_chart_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/question-statistics'),
          ),
          IconButton(
            icon: const Icon(Icons.history_rounded),
            onPressed: () => context.push('/question-version-history'),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: AppColors.accentTeal.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
                child: const Text('TYPE: MCQ', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 11)),
              ),
              const SizedBox(width: 8),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: AppColors.accentIndigo.withOpacity(0.2), borderRadius: BorderRadius.circular(6)),
                child: const Text('CONCEPT: DSA_ARRAYS_01', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 11)),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text('Array Index Offset Calculation', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 16),
          AppCard(
            child: const Text(
              'Given base address 0x1000 and element size 4 bytes, calculate address of index 5.',
              style: TextStyle(color: Colors.white, fontSize: 14),
            ),
          ),
          const SizedBox(height: 16),

          // Misconceptions Detected
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Misconceptions Detected', style: TextStyle(color: AppColors.warning, fontWeight: FontWeight.bold, fontSize: 15)),
                Divider(color: AppColors.darkBorder),
                Text('MIS_OFFSET_01: Multiplying base address instead of stride.', style: TextStyle(color: Colors.white, fontSize: 12)),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Potential Root Causes
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Root Causes Diagnosed', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 15)),
                Divider(color: AppColors.darkBorder),
                Text('1. Concept Gap: Pointer arithmetic formula confusion (Weight: 0.85)', style: TextStyle(color: Colors.white, fontSize: 12)),
                Text('2. Calculation Error: Arithmetic multiplication mismatch (Weight: 0.60)', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
              ],
            ),
          ),
          const SizedBox(height: 24),
          ElevatedButton.icon(
            onPressed: () => context.push('/question-preview'),
            icon: const Icon(Icons.play_arrow_rounded),
            label: const Text('Interactive Question Preview & Hints'),
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
