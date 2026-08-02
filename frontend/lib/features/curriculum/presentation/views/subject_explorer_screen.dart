import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/curriculum/presentation/controllers/curriculum_controller.dart';

class SubjectExplorerScreen extends ConsumerWidget {
  const SubjectExplorerScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(subjectProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Subject Explorer'),
        actions: [
          IconButton(
            icon: const Icon(Icons.hub_outlined, color: AppColors.accentTeal),
            onPressed: () => context.push('/knowledge-graph-viewer'),
          ),
          IconButton(
            icon: const Icon(Icons.search_rounded),
            onPressed: () => context.push('/curriculum-search'),
          ),
        ],
      ),
      body: state.isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.accentTeal))
          : ListView(
              padding: const EdgeInsets.all(24),
              children: [
                Text(
                  'Educational Domains',
                  style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white),
                ),
                const SizedBox(height: 8),
                Text(
                  'Select a subject domain to explore chapters, topics, and prerequisite concept DAGs.',
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(color: AppColors.textSecondaryDark),
                ),
                const SizedBox(height: 24),
                _buildSubjectCard(context, 'Data Structures & Algorithms', 'DSA', 'Core CS memory layouts, trees & graphs', Icons.code_rounded),
                const SizedBox(height: 16),
                _buildSubjectCard(context, 'Mathematics', 'MATH', 'Calculus, linear algebra & differential equations', Icons.functions_rounded),
                const SizedBox(height: 16),
                _buildSubjectCard(context, 'Physics', 'PHYS', 'Classical mechanics, thermodynamics & electromagnetism', Icons.science_outlined),
                const SizedBox(height: 16),
                _buildSubjectCard(context, 'Chemistry', 'CHEM', 'Chemical bonding, organic chemistry & stoichiometry', Icons.biotech_outlined),
                const SizedBox(height: 16),
                _buildSubjectCard(context, 'General Science', 'SCI', 'Cellular biology, genetics & ecosystems', Icons.eco_outlined),
              ],
            ),
    );
  }

  Widget _buildSubjectCard(BuildContext context, String title, String code, String desc, IconData icon) {
    return AppCard(
      onTap: () => context.push('/chapters-explorer?code=$code'),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: AppColors.accentTeal.withOpacity(0.15),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: AppColors.accentTeal, size: 32),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: AppColors.accentIndigo.withOpacity(0.2),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(code, style: const TextStyle(color: AppColors.accentCyan, fontSize: 10, fontWeight: FontWeight.bold)),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(desc, style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
