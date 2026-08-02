import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/shared/widgets/custom_button.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/diagnosis/presentation/controllers/diagnosis_controller.dart';

class AnswerSubmissionScreen extends ConsumerStatefulWidget {
  const AnswerSubmissionScreen({super.key});

  @override
  ConsumerState<AnswerSubmissionScreen> createState() => _AnswerSubmissionScreenState();
}

class _AnswerSubmissionScreenState extends ConsumerState<AnswerSubmissionScreen> {
  final _answerController = TextEditingController(text: "0x1005");

  void _handleAnalyze() async {
    final success = await ref.read(diagnosisProvider.notifier).submitForDiagnosis(
          studentId: "11111111-1111-1111-1111-111111111111",
          questionId: "q1_arrays_01",
          answer: _answerController.text.trim(),
          timeSpentSeconds: 45,
          hintsUsed: 1,
        );

    if (mounted && success) {
      context.push('/diagnosis-report');
    }
  }

  @override
  Widget build(BuildContext context) {
    final state = ref.watch(diagnosisProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('BACKTRACE Diagnostic Terminal')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Submit Solution for Root-Cause Diagnosis', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('The BACKTRACE Intelligence Engine will evaluate your submission and diagnose the root cause behind any misconceptions.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Q: Array Index Offset Calculation (DSA_ARRAYS_01)', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 13)),
                SizedBox(height: 8),
                Text('Given base address 0x1000 and element size 4 bytes, calculate address of index 5.', style: TextStyle(color: Colors.white, fontSize: 14)),
              ],
            ),
          ),
          const SizedBox(height: 24),
          TextField(
            controller: _answerController,
            decoration: InputDecoration(
              labelText: 'Your Solution / Answer',
              filled: true,
              fillColor: AppColors.darkCard,
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
          ),
          const SizedBox(height: 24),
          SizedBox(
            width: double.infinity,
            child: CustomButton(
              label: 'Run Root-Cause Diagnosis',
              isLoading: state.isAnalyzing,
              onPressed: _handleAnalyze,
              icon: Icons.psychology_outlined,
            ),
          ),
        ],
      ),
    );
  }
}
