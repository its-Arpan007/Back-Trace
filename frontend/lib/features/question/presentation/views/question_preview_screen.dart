import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/shared/widgets/custom_button.dart';

class QuestionPreviewScreen extends StatefulWidget {
  const QuestionPreviewScreen({super.key});

  @override
  State<QuestionPreviewScreen> createState() => _QuestionPreviewScreenState();
}

class _QuestionPreviewScreenState extends State<QuestionPreviewScreen> {
  int _unlockedHintLevel = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Interactive Question Preview')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Q: Array Index Offset Calculation', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                SizedBox(height: 8),
                Text('Given base address 0x1000 and element size 4 bytes, calculate address of index 5.', style: TextStyle(color: AppColors.textSecondaryDark)),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Options
          _buildOptionTile('A', '0x1014 (Base + 5 * 4 = 0x1000 + 20)'),
          const SizedBox(height: 8),
          _buildOptionTile('B', '0x1005 (Base + 5)'),
          const SizedBox(height: 8),
          _buildOptionTile('C', '0x1020 (Base + 5 * 8)'),

          const SizedBox(height: 24),
          if (_unlockedHintLevel > 0)
            AppCard(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Hint Level $_unlockedHintLevel Unlocked', style: const TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 4),
                  const Text('Remember formula: Offset = Base + (Index * ElementSize).', style: TextStyle(color: Colors.white)),
                ],
              ),
            ),
          const SizedBox(height: 12),
          OutlinedButton.icon(
            onPressed: () => setState(() => _unlockedHintLevel = (_unlockedHintLevel + 1).clamp(0, 3)),
            icon: const Icon(Icons.lightbulb_outline, color: AppColors.accentTeal),
            label: Text('Request Hint (Level ${_unlockedHintLevel + 1})', style: const TextStyle(color: AppColors.accentTeal)),
          ),
          const SizedBox(height: 24),
          SizedBox(
            width: double.infinity,
            child: CustomButton(
              label: 'Submit Answer',
              onPressed: () {},
              icon: Icons.check_rounded,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildOptionTile(String letter, String text) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(color: AppColors.darkCard, borderRadius: BorderRadius.circular(12), border: Border.all(color: AppColors.darkBorder)),
      child: Row(
        children: [
          CircleAvatar(radius: 14, backgroundColor: AppColors.accentTeal, child: Text(letter, style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.bold))),
          const SizedBox(width: 12),
          Expanded(child: Text(text, style: const TextStyle(color: Colors.white, fontSize: 13))),
        ],
      ),
    );
  }
}
