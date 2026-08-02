import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class KnowledgeDecayViewScreen extends StatelessWidget {
  const KnowledgeDecayViewScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Knowledge Decay Curve')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: const [
            AppCard(
              child: ListTile(
                leading: Icon(Icons.show_chart_rounded, color: AppColors.warning, size: 36),
                title: Text('Predicted Decay: 12%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: Text('Days Since Last Practice: 3 Days • Forgetting Curve Model Active', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
