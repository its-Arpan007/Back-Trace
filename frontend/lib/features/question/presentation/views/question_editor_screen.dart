import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/shared/widgets/custom_button.dart';

class QuestionEditorScreen extends StatelessWidget {
  const QuestionEditorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Intelligence Editor')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          TextField(
            decoration: InputDecoration(
              labelText: 'Question Title',
              filled: true,
              fillColor: AppColors.darkCard,
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
          ),
          const SizedBox(height: 16),
          TextField(
            maxLines: 4,
            decoration: InputDecoration(
              labelText: 'Question Statement (Markdown / LaTeX supported)',
              filled: true,
              fillColor: AppColors.darkCard,
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
          ),
          const SizedBox(height: 16),
          TextField(
            decoration: InputDecoration(
              labelText: 'Primary Concept Code (e.g. DSA_ARRAYS_01)',
              filled: true,
              fillColor: AppColors.darkCard,
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
          ),
          const SizedBox(height: 24),
          SizedBox(
            width: double.infinity,
            child: CustomButton(
              label: 'Save & Publish Question',
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Question published to Intelligence Bank'), backgroundColor: AppColors.success),
                );
              },
              icon: Icons.publish_rounded,
            ),
          ),
        ],
      ),
    );
  }
}
