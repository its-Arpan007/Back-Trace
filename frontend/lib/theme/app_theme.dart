import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/theme/app_typography.dart';

class AppTheme {
  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      scaffoldBackgroundColor: AppColors.darkBackground,
      colorScheme: const ColorScheme.dark(
        primary: AppColors.accentTeal,
        secondary: AppColors.accentIndigo,
        surface: AppColors.darkSurface,
        background: AppColors.darkBackground,
        error: AppColors.error,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: AppColors.darkSurface,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: AppTypography.titleLarge(AppColors.textPrimaryDark),
      ),
      cardTheme: CardTheme(
        color: AppColors.darkCard,
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: const BorderSide(color: AppColors.darkBorder, width: 1),
        ),
      ),
      textTheme: TextTheme(
        displayLarge: AppTypography.displayLarge(AppColors.textPrimaryDark),
        displayMedium: AppTypography.displayMedium(AppColors.textPrimaryDark),
        titleLarge: AppTypography.titleLarge(AppColors.textPrimaryDark),
        bodyLarge: AppTypography.bodyLarge(AppColors.textPrimaryDark),
        bodyMedium: AppTypography.bodyMedium(AppColors.textSecondaryDark),
        labelSmall: AppTypography.labelSmall(AppColors.textSecondaryDark),
      ),
    );
  }

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      scaffoldBackgroundColor: AppColors.lightBackground,
      colorScheme: const ColorScheme.light(
        primary: AppColors.primary,
        secondary: AppColors.accentTeal,
        surface: AppColors.lightSurface,
        background: AppColors.lightBackground,
        error: AppColors.error,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: AppColors.lightSurface,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: AppTypography.titleLarge(AppColors.textPrimaryLight),
      ),
      cardTheme: CardTheme(
        color: AppColors.lightCard,
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: const BorderSide(color: AppColors.lightBorder, width: 1),
        ),
      ),
      textTheme: TextTheme(
        displayLarge: AppTypography.displayLarge(AppColors.textPrimaryLight),
        displayMedium: AppTypography.displayMedium(AppColors.textPrimaryLight),
        titleLarge: AppTypography.titleLarge(AppColors.textPrimaryLight),
        bodyLarge: AppTypography.bodyLarge(AppColors.textPrimaryLight),
        bodyMedium: AppTypography.bodyMedium(AppColors.textSecondaryLight),
        labelSmall: AppTypography.labelSmall(AppColors.textSecondaryLight),
      ),
    );
  }
}
