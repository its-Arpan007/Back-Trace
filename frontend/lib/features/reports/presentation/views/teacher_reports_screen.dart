import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class TeacherReportsScreen extends StatelessWidget {
  const TeacherReportsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Classroom Analytics & Report Generator')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.picture_as_pdf_rounded, color: AppColors.accentTeal),
              title: Text('Classroom Misconception Frequency Audit Report', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Format: PDF / CSV Export Ready • Contains student weakness matrix.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
