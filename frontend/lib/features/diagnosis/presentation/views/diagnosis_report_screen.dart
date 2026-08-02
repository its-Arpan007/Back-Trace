import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/diagnosis/presentation/controllers/diagnosis_controller.dart';

class DiagnosisReportScreen extends ConsumerWidget {
  const DiagnosisReportScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(diagnosisProvider);
    final report = state.activeReport;

    final primaryCause = report?['primary_root_cause'] ?? 'Concept Gap';
    final confidence = report?['confidence_score'] ?? 91.5;
    final conceptCode = report?['concept_code'] ?? 'DSA_ARRAYS_01';
    final procTime = report?['processing_time_ms'] ?? 142.0;

    return Scaffold(
      appBar: AppBar(
        title: const Text('BACKTRACE Diagnosis Report'),
        actions: [
          IconButton(
            icon: const Icon(Icons.history_rounded),
            onPressed: () => context.push('/diagnosis-history'),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              StatusBadge(label: 'DIAGNOSIS COMPLETE', isOnline: true),
              Text('${procTime}ms', style: const TextStyle(color: AppColors.accentCyan, fontSize: 12, fontWeight: FontWeight.bold)),
            ],
          ),
          const SizedBox(height: 16),

          // Primary Root Cause Card
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('PRIMARY ROOT CAUSE DIAGNOSED', style: TextStyle(color: AppColors.error, fontWeight: FontWeight.bold, fontSize: 12, letterSpacing: 1.2)),
                const SizedBox(height: 8),
                Text(primaryCause, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 20)),
                const SizedBox(height: 12),
                Row(
                  children: [
                    const Icon(Icons.verified_outlined, color: AppColors.accentTeal, size: 18),
                    const SizedBox(width: 6),
                    Text('Confidence: ${confidence}%', style: const TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold)),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Action Navigation Buttons
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => context.push('/evidence-viewer'),
                  icon: const Icon(Icons.receipt_long_rounded, size: 16),
                  label: const Text('Evidence'),
                  style: ElevatedButton.styleFrom(backgroundColor: AppColors.darkCard),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => context.push('/weak-concept-viewer'),
                  icon: const Icon(Icons.account_tree_rounded, size: 16),
                  label: const Text('Weak Chain'),
                  style: ElevatedButton.styleFrom(backgroundColor: AppColors.darkCard),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => context.push('/misconception-viewer'),
                  icon: const Icon(Icons.bug_report_rounded, size: 16),
                  label: const Text('Misconception'),
                  style: ElevatedButton.styleFrom(backgroundColor: AppColors.darkCard),
                ),
              ),
            ],
          ),
          const SizedBox(height: 24),

          // Next Recommended Remediation Actions
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Recommended Remediation Actions', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                const Divider(color: AppColors.darkBorder),
                const SizedBox(height: 8),
                ListTile(
                  leading: const Icon(Icons.play_circle_fill_rounded, color: AppColors.accentTeal),
                  title: const Text('Review Lesson: Array Memory Stride Calculation', style: TextStyle(color: Colors.white, fontSize: 13)),
                  trailing: const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textSecondaryDark, size: 14),
                ),
                ListTile(
                  leading: const Icon(Icons.quiz_rounded, color: AppColors.accentCyan),
                  title: const Text('Retest: Pointer Offset Retest Question', style: TextStyle(color: Colors.white, fontSize: 13)),
                  trailing: const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textSecondaryDark, size: 14),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
