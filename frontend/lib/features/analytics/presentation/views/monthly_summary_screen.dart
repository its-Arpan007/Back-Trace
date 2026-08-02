import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class MonthlySummaryScreen extends StatelessWidget {
  const MonthlySummaryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Monthly Learning Summary')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              title: Text('Monthly Mastery Growth: +34%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Active Streak: 28 Days • Total Modules Completed: 3', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
